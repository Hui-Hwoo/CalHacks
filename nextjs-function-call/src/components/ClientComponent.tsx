"use client";
import {
    VoiceProvider,
    ToolCall,
    ToolCallHandler,
    ToolResponse,
    ToolError,
} from "@humeai/voice-react";
import Messages from "./Controls";
import Controls from "./Messages";

const handleToolCall: ToolCallHandler = async (
    toolCall: ToolCall
): Promise<ToolResponse | ToolError> => {
    console.log("Tool call received", toolCall);
    if (toolCall.name === "getFlashcards") {
        try {
            // parsing the parameters
            const args = JSON.parse(toolCall.parameters) as {
                deckName: string;
                onlyDue: boolean;
            };

            const flashcards = {
                "1": ["What color is the sky on a clear day?", "Blue", 3],
                "2": ["What do you use to write or draw?", "A pencil", 1],
                "3": ["What is the opposite of hot?", "Cold", 4],
                "4": ["What do you call a baby cat?", "A kitten", 2],
                "5": [
                    "What is the name of the tree that produces acorns?",
                    "Oak",
                    3,
                ],
            };

            const flashcards_bio = {
                "6": ["What liquid do most plants need to grow?", "Water", 2],
                "7": [
                    "What do you wear on your feet to go outside?",
                    "Shoes",
                    1,
                ],
                "8": ["What do bees make?", "Honey", 4],
                "9": ["What is the main ingredient in bread?", "Flour", 3],
                "10": [
                    "What do you call the star at the center of our solar system?",
                    "The Sun",
                    2,
                ],
            };

            // return object
            return {
                type: "tool_response",
                tool_call_id: toolCall.tool_call_id,
                content: JSON.stringify(
                    args.deckName == "Physics" ? flashcards : flashcards_bio
                ),
            };
        } catch (error) {
            return {
                type: "tool_error",
                tool_call_id: toolCall.tool_call_id,
                error: "Get flashcards tool error",
                code: "get_flashcards_tool_error",
                level: "warn",
                content: "There was an error with the getting flashcards",
            };
        }
    } else if (toolCall.name === "setAnswers") {
        try {
            // parsing the parameters
            const args = JSON.parse(toolCall.parameters) as {
                answers: Array<object>;
            };
            // TODO save args to the file in the appropriate format
            // return object
            return {
                type: "tool_response",
                tool_call_id: toolCall.tool_call_id,
                content: "done!",
            };
        } catch (error) {
            return {
                type: "tool_error",
                tool_call_id: toolCall.tool_call_id,
                error: "Get flashcards tool error",
                code: "get_flashcards_tool_error",
                level: "warn",
                content: "There was an error with the getting flashcards",
            };
        }
    } else {
        return {
            type: "tool_error",
            tool_call_id: toolCall.tool_call_id,
            error: "Tool not found",
            code: "tool_not_found",
            level: "warn",
            content: "The tool you requested was not found",
        };
    }
};

export default function ClientComponent({
    accessToken,
}: {
    accessToken: string;
}) {
    return (
        <VoiceProvider
            configId={process.env.NEXT_PUBLIC_HUME_CONFIG_ID}
            auth={{ type: "accessToken", value: accessToken }}
            onToolCall={handleToolCall}
            onMessage={(message: unknown) => console.log(message)}
        >
            <Messages />
            <Controls />
        </VoiceProvider>
    );
}

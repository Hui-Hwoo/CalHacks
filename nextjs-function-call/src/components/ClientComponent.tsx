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
  if (toolCall.name === 'getFlashcards') {
    try {
      // parsing the parameters
      const args = JSON.parse(toolCall.parameters) as {
        deckName: string;
        onlyDue: boolean;
      };
      const flashcards = {
        "1": ["What is the name of our star?", "The Sun", 3],
        "2": ["What is pi to 2 decimal points?", "2", 1]
      }
      const flashcards_bio = {
        "1": ["Is plasma a component of blood?", "Yes", 4],
        "2": ["Name of powerhouse of the cell?", "Mitochondria", 2]
      }

      // return object
      return {
        type: 'tool_response',
        tool_call_id: toolCall.tool_call_id,
        content: JSON.stringify((args.deckName =="Physics") ? flashcards: flashcards_bio),
      };
    } catch (error) {
      return {
        type: 'tool_error',
        tool_call_id: toolCall.tool_call_id,
        error: 'Get flashcards tool error',
        code: 'get_flashcards_tool_error',
        level: 'warn',
        content: 'There was an error with the getting flashcards',
      };
    }
  } else if (toolCall.name === 'setAnswers') {
    try {
      // parsing the parameters
      const args = JSON.parse(toolCall.parameters) as {
        answers: Array<object>;
      };
      // TODO save args to the file in the appropriate format
      // return object
      return {
        type: 'tool_response',
        tool_call_id: toolCall.tool_call_id,
        content: "done!",
      };
    } catch (error) {
      return {
        type: 'tool_error',
        tool_call_id: toolCall.tool_call_id,
        error: 'Get flashcards tool error',
        code: 'get_flashcards_tool_error',
        level: 'warn',
        content: 'There was an error with the getting flashcards',
      };
    }
  }
  else {
    return {
      type: 'tool_error',
      tool_call_id: toolCall.tool_call_id,
      error: 'Tool not found',
      code: 'tool_not_found',
      level: 'warn',
      content: 'The tool you requested was not found',
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

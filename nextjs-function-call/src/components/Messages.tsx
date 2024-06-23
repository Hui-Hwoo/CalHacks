"use client";
import { useVoice } from "@humeai/voice-react";
import { useMemo } from "react";

function capitalizeFirstLetter(s) {
  return s.charAt(0).toUpperCase() + s.slice(1);
}

export default function Controls() {
  const { messages } = useVoice();
  type MessageType = "user_message" | "assistant_message";

  interface Message {
    type: MessageType;
    message: {
      role: "assistant" | "user";
      content: string;
    };
  }

  interface GroupedMessage {
    role: "assistant" | "user";
    content: string[];
  }

  // Function to group continuous messages by the same role
  const groupedMessages: GroupedMessage[] = useMemo(() => {
    const grouped: GroupedMessage[] = [];
    let currentGroup: GroupedMessage | null = null;

    messages.forEach((msg) => {
      if (msg.type === "user_message" || msg.type === "assistant_message") {
        if (currentGroup && currentGroup.role === msg.message.role) {
          currentGroup.content.push(msg.message.content);
        } else {
          if (currentGroup) {
            grouped.push(currentGroup);
          }
          currentGroup = {
            role: msg.message.role,
            content: [msg.message.content],
          };
        }
      } else {
        if (currentGroup) {
          grouped.push(currentGroup);
          currentGroup = null;
        }
      }
    });

    if (currentGroup) {
      grouped.push(currentGroup);
    }

    return grouped;
  }, [messages]);

  return (
    <div>
      {groupedMessages.map((group, index) => (
        <div
          className={
            "py-8 px-8 max-w-sm mx-auto mb-5 border-2 bg-gray rounded-xl  sm:py-4 sm:flex sm:items-center sm:space-y-0 sm:space-x-6 " +
            (group.role === "assistant" ? "border-amber-200" : "border-lime-200")
          }
          key={index}
        >
          <div className="role text-slate-400 text-sm">
            {capitalizeFirstLetter(group.role === "assistant" ? "Aido" : "Me")}
          </div>
          <div className="content">
            {group.content.map((text, i) => (
              <div key={i}>{text}</div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

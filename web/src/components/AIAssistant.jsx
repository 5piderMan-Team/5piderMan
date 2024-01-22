import { FloatButton } from "antd";
import {
  CommentOutlined,
  SendOutlined,
  RobotOutlined,
  UserOutlined,
  UndoOutlined,
} from "@ant-design/icons";
import { useEffect, useState } from "react";
import { Input, Button } from "antd";
const { TextArea } = Input;
import * as Api from "../backend/job";
import { useSessionStorageState, useCounter } from "ahooks";
// message: { type: "user" | "ai", content: string }

const AIMessage = ({ message }) => {
  return (
    <div className="flex justify-start mb-4">
      {/* avatar */}
      <RobotOutlined />
      {/* message */}
      <div className="bg-white ml-2 p-2 rounded-sm shadow-sm shadow-gray-600 max-w-xs">
        {message}
      </div>
    </div>
  );
};

const UserMessage = ({ message }) => {
  return (
    <div className="flex justify-end mb-4">
      {/* message */}
      <div className="bg-blue-400 mr-2 p-2 rounded-sm shadow-sm shadow-gray-600 max-w-xs">
        {message}
      </div>
      {/* avatar */}
      <UserOutlined />
    </div>
  );
};

const ShowMessages = ({ messages, thinking = false }) => {
  return (
    <div className="flex flex-col flex-grow p-4 overflow-y-auto">
      {messages.map((message) => {
        if (message.type === "ai") {
          return <AIMessage message={message.content} key={message.key} />;
        } else {
          return <UserMessage message={message.content} key={message.key} />;
        }
      })}
      {thinking && <AIMessage message="thinking..." />}
    </div>
  );
};

/*
{
  "output": "正在为您跳转到Python搜索页面",
  "type": "search",
  "content": "Python"
}
*/
const handleGPTFunctionCall = (res) => {
  console.log(res);
  if (res.type === null || res.type === "") {
    return res.output;
  }

  switch (res.type) {
    case "search":
      new Promise((resolve, reject) => {
        setTimeout(() => {
          window.location.href = `/search?keyword=${res.content}`;
          resolve();
        }, 1000);
      });
      return "正在为您跳转到 " + res.content + " 搜索页面";
    case "city":
      new Promise((resolve, reject) => {
        setTimeout(() => {
          window.location.href = `/?city=${res.content}`;
          resolve();
        }, 1000);
      });
      return "正在为您跳转到 " + res.content + " 工作页面";
    default:
      return "未知操作： " + res.type + " " + res.content;
  }
};

const AIAssistant = () => {
  const [visible, setVisible] = useState(false);
  const [messages, setMessages] = useSessionStorageState("messages", {
    defaultValue: [{ type: "ai", content: "你好，很荣幸为你服务", key: 0 }],
  });
  const [input, setInput] = useState("");
  const [canSand, setCanSand] = useState(true);
  const [current, { inc }] = useCounter(1);

  useEffect(() => {
    if (!canSand) {
      setInput("");
      Api.getGPTRespond(input)
        .then((res) => {
          return handleGPTFunctionCall(res);
        })
        .then((res) => {
          setMessages([
            ...messages,
            { type: "ai", content: res, key: current },
          ]);
          inc();
          setCanSand(true);
        });
    }
  }, [canSand]);

  const onClick = () => {
    setVisible(!visible);
  };

  const onSend = () => {
    // console.log(input);
    setMessages([...messages, { type: "user", content: input, key: current }]);
    inc();
    setCanSand(false);
  };

  const clearMessages = () => {
    setMessages([{ type: "ai", content: "你好，很荣幸为你服务", key: 0 }]);
  };

  return (
    <>
      <div style={{ display: visible ? "block" : "none" }}>
        <div className="fixed bottom-24 right-8 w-1/3 h-2/3   bg-blue-100 rounded-xl shadow-lg shadow-gray-300">
          <div className="flex flex-col h-full">
            <div className="flex flex-row justify-between items-center p-4 border-b border-gray-300">
              <div className="text-lg font-bold">AI小助手</div>
            </div>
            <ShowMessages messages={messages} thinking={!canSand} />
            <div className="flex flex-row justify-between items-center ml-8 mr-8 mb-4">
              <Button
                type="primary"
                shape="circle"
                icon={<UndoOutlined />}
                onClick={clearMessages}
              />
              <TextArea
                showCount
                maxLength={100}
                placeholder="请输入"
                style={{
                  height: 60,
                  resize: "none",
                  marginLeft: 16,
                  marginRight: 16,
                }}
                value={input}
                onInput={(e) => {
                  setInput(e.target.value);
                }}
              />
              <Button
                type="primary"
                shape="circle"
                icon={<SendOutlined />}
                onClick={onSend}
                disabled={!canSand}
              />
            </div>
          </div>
        </div>
      </div>
      <FloatButton
        icon={<CommentOutlined />}
        tooltip="AI小助手"
        onClick={onClick}
      ></FloatButton>
    </>
  );
};

export default AIAssistant;

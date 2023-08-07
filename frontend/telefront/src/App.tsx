import React, { useState, FC } from "react";
import logo from "./logo.svg";
import "./App.css";
import Card from "./components/Card";
import { Login, Verification } from "./utils/flaskApi";
import LoginForm from "./modules/LoginForm";
import VerificationForm from "./modules/VerificationForm";

const App: FC = () => {
  const [login, setLogin] = useState<string>();

  const handeVerificationSubmit = async (verificationCode: string) => {
    const data = await Verification(verificationCode);
  };
  const handleLoginSubmit = async (
    apiId: string,
    apiHash: string,
    phoneNumber: string
  ) => {
    const data = await Login(apiId, apiHash, phoneNumber);
    //data && setLogin(data);z
  };
  return (
    <div className="container px-6 mx-auto mt-10">
      <h1 className="mb-10 text-4xl font-extrabold leading-none tracking-tight text-center text-gray-900 md:text-5xl lg:text-6xl">
        Telegram Bot Creator
      </h1>

      <div className="gap-6 sm:flex sm:flex-col">
        <Card className="w">
          <LoginForm onSubmit={handleLoginSubmit} />
        </Card>

        <Card className="w">
          <VerificationForm onSubmit={handeVerificationSubmit} />
        </Card>
      </div>
    </div>
  );
};

export default App;

import { ButtonHTMLAttributes, FC, PropsWithChildren } from "react";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {}

const Button: FC<PropsWithChildren<Props>> = ({ children, ...props }) => {
  return (
    <button
      className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 focus:outline-none"
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;

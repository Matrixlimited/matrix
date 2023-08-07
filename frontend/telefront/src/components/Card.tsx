import { FC, HTMLAttributes, PropsWithChildren } from "react";

interface Props extends HTMLAttributes<HTMLDivElement> {}

const Card: FC<PropsWithChildren<Props>> = ({
  children,
  className,
  ...props
}) => {
  return (
    <div
      className={`block p-6 bg-white border border-gray-200 rounded-lg shadow ${
        className || ""
      }`}
      {...props}
    >
      {children}
    </div>
  );
};

export default Card;

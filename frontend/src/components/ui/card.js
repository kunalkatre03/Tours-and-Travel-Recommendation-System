export function Card({ title, children }) {
    return (
      <div className="border shadow-md p-4 rounded-lg bg-white">
        <h2 className="text-lg font-bold">{title}</h2>
        <div>{children}</div>
      </div>
    );
  }
  
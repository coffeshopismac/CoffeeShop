import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="flex justify-between py-3 items-center">
      <Link to="/tasks">
<<<<<<< HEAD
        <h1 className="font-bold text-3xl mb-4">CoffeeShopIsmac</h1>
      </Link>
     
      <button className="bg-green-500 p-3 rounded-lg">
          <Link to="/clientes">Ver Clientes</Link>
        </button>
=======
        <h1 className="font-bold text-3xl mb-4">Tasks App</h1>
      </Link>
      <button className="bg-indigo-500 p-3 rounded-lg">
        <Link to="/tasks-create">Create Task</Link>
      </button>
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
    </div>
  );
}
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { TaskFormPage } from "./pages/TaskFormPage";
import { TasksPage } from "./pages/TasksPage";
<<<<<<< HEAD
import { ClientesPage } from "./pages/ClientesPage";
import { ClienteForm } from "./pages/ClienteForm";  // Asegúrate de que la ruta sea correcta
=======
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Navigation />
        <Routes>
          {/* redirect to tasks */}
          <Route path="/" element={<Navigate to="/tasks" />} />
          <Route path="/tasks" element={<TasksPage />} />
          <Route path="/tasks-create" element={<TaskFormPage />} />
          <Route path="/tasks/:id" element={<TaskFormPage />} />
<<<<<<< HEAD
          <Route path="/clientes" element={<ClientesPage />} /> {/* Ruta para ClientesPage */}
          <Route path="/clientes/:id" element={<ClientesPage />} /> {/* Ruta para ver cliente individual si es necesario */}
          <Route path="/clientes-create" element={<ClienteForm />} />  {/* Ruta para crear cliente */}
=======
>>>>>>> a1208405d428e12e418b775e30138426a17d67f5
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;
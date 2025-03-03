import { useState } from "react";
import ApiService from "../api/tasks.api";  // Asegúrate de que ApiService tenga el método para crear el cliente
import { useNavigate } from "react-router-dom";  // Para redirigir después de la creación

export function ClienteForm() {
  const [clienteData, setClienteData] = useState({
    nombre: "",
    apellido: "",
    telefono: "",
    direccion: "", // Asegúrate de que esta propiedad esté en el estado inicial
    correo: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();  // Para redirigir después de agregar el cliente

  const handleChange = (e) => {
    const { name, value } = e.target;
    setClienteData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Llamar a la API para crear el cliente
      await ApiService.createCliente(clienteData);
      setLoading(false);
      navigate("/task/clientes");  // Redirigir a la página de clientes
    } catch (err) {
      setError("Hubo un error al crear el cliente.");
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Registrar Nuevo Cliente</h1>

      {error && <p className="text-red-500">{error}</p>}

      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="nombre" className="block text-sm font-semibold">Nombre</label>
          <input
            type="text"
            id="nombre"
            name="nombre"
            value={clienteData.nombre}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded mt-1 text-black" // Añadir text-black
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="apellido" className="block text-sm font-semibold">Apellido</label>
          <input
            type="text"
            id="apellido"
            name="apellido"
            value={clienteData.apellido}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded mt-1 text-black" // Añadir text-black
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="telefono" className="block text-sm font-semibold">Teléfono</label>
          <input
            type="text"
            id="telefono"
            name="telefono"
            value={clienteData.telefono}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded mt-1 text-black" // Añadir text-black
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="direccion" className="block text-sm font-semibold">Dirección</label>
          <input
            type="text"
            id="direccion"
            name="direccion"
            value={clienteData.direccion}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded mt-1 text-black" // Añadir text-black
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="correo" className="block text-sm font-semibold">Correo</label>
          <input
            type="email"
            id="correo"
            name="correo"
            value={clienteData.correo}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded mt-1 text-black" // Añadir text-black
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className={`w-full py-2 bg-blue-500 text-white rounded ${loading && "opacity-50"}`}
        >
          {loading ? "Registrando..." : "Registrar Cliente"}
        </button>
      </form>
    </div>
  );
}
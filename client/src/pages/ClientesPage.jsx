import React from "react";
import { useEffect, useState } from "react";
import ApiService from "../api/tasks.api";  // Importa el servicio API
import { Link } from "react-router-dom";  // Enlace para navegar si es necesario



export function ClientesPage() {
    const [clientes, setClientes] = useState([]);
  
    useEffect(() => {
      const fetchClientes = async () => {
        try {
          const res = await ApiService.getClientes();  // Obtener clientes desde la API
          setClientes(res.data);  // Almacenar los datos en el estado
        } catch (error) {
          console.error("Error al obtener clientes", error);
        }
      };
      fetchClientes();
    }, []);  // Solo se ejecuta una vez cuando el componente se monta

     // Función para manejar la creación de un cliente
  const handleClienteCreated = async () => {
    const res = await ApiService.getClientes(); // Obtener la lista actualizada de clientes
    setClientes(res.data);  // Actualizar la lista de clientes en el estado
    };
  
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-4">Clientes</h1>

         {/* Botón para registrar un nuevo cliente */}
      <div className="mb-4">
        <Link to="/clientes-create">
          <button className="bg-blue-500 text-white py-2 px-4 rounded">Registrar Nuevo Cliente</button>
        </Link>
      </div>
  
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          {/* Si no hay clientes, muestra un mensaje */}
          {clientes.length === 0 ? (
            <p>Cargando clientes...</p>
          ) : (
            clientes.map((cliente) => (
              <div key={cliente.cliente_id} className="border p-4 rounded shadow">
                <p><strong>Nombre:</strong> {cliente.nombre}</p>
                <p><strong>Apellido:</strong> {cliente.apellido}</p>
                <p><strong>Teléfono:</strong> {cliente.telefono}</p>
                <p><strong>Dirección:</strong> {cliente.direccion}</p>
                <p><strong>Email:</strong> {cliente.email}</p>
              </div>
            ))
          )}
        </div>
      </div>
    );
  }
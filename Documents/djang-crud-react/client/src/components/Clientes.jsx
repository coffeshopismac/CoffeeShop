import React, { useEffect, useState } from "react";
import tasksApi from "../api/tasks.api.js"; // Importa ApiService desde la carpeta correcta

const Clientes = () => {
  const [clientes, setClientes] = useState([]);

  useEffect(() => {
    tasksApi.getClientes()
      .then(response => setClientes(response.data))
      .catch(error => console.error("Error al obtener clientes:", error));
  }, []);

  return (
    <div>
      <h2>Lista de Clientes</h2>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Teléfono</th>
            <th>Direcion</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map(cliente => (
            <tr key={cliente.id}>
              <td>{cliente.id}</td>
              <td>{cliente.nombre}</td>
              <td>{cliente.apellido}</td>
              <td>{cliente.telefono}</td>
              <td>{cliente.direccion}</td>
              <td>{cliente.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Clientes;

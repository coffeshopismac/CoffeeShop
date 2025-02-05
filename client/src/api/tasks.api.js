import axios from "axios";

const URL =
  process.env.NODE_ENV === "production"
    ? import.meta.env.VITE_BACKEND_URL
    : "http://localhost:8000";

console.log(URL);
const tasksApi = axios.create({
  baseURL: `${URL}/api/v1`,  // Cambiado a /api/v1
});

export const getAllTasks = () => tasksApi.get("/tasks/");  // Cambiado a /tasks/
export const getTask = (id) => tasksApi.get(`/tasks/${id}/`);  // Cambiado a /tasks/${id}/
export const createTask = (task) => tasksApi.post("/tasks/", task);  // Cambiado a /tasks/
export const updateTask = (id, task) => tasksApi.put(`/tasks/${id}/`, task);  // Cambiado a /tasks/${id}/
export const deleteTask = (id) => tasksApi.delete(`/tasks/${id}/`);  // Cambiado a /tasks/${id}/
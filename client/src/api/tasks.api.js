import axios from "axios";

const tasksApi = axios.create({
  baseURL: "http://localhost:8000/api/v1/tasks/" // Corrige la baseURL
});

export const getAllTasks = () => tasksApi.get("/");

export const createTask = (task) => tasksApi.post("/", task);
import { useForm } from 'react-hook-form'; // Corregido "useform" a "useForm" y ajustado el espaciado
import { createTask } from '../api/tasks.api'; // Aseguradas las comillas y el espaciado

export function TasksFormPage() {
  const { 
    register, 
    handleSubmit, 
    formState: { errors } // Ajustado el espaciado y formato
  } = useForm();

  const onSubmit = handleSubmit(async (data) => {
    const res = await createTask(data); // Asegurada la indentación y el espaciado
    console.log(res);
  });

  return (
    <div>
      <form onSubmit={onSubmit}>
        <input 
          type="text" 
          placeholder="Title" 
          {...register("title", { required: true })}
        />
        {errors.title && <span>Title is required</span>} {/* Ajustada la capitalización del texto */}
        
        <textarea 
          rows="3" 
          placeholder="Description" 
          {...register("description", { required: true })}
        ></textarea>
        {errors.description && <span>Description is required</span>} {/* Ajustada la capitalización del texto */}
        
        <button>Save</button>
      </form>
    </div>
  );
}

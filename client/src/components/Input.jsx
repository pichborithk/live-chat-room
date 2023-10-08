/* eslint-disable react/prop-types */

const Input = ({ value, setValue, required, name, type, label }) => {
  return (
    <fieldset className='flex w-full flex-col gap-2'>
      <label htmlFor={name}>{label}</label>
      <input
        className='rounded-md py-2 px-4 focus:outline-sky-600 focus:outline-2 text-sky-600'
        name={name}
        type={type}
        id={name}
        required={required}
        value={value}
        onChange={event => setValue(event.target.value)}
      />
    </fieldset>
  );
};
export default Input;

const ChatRoom = () => {
  return (
    <div className='shadow-full w-full p-4 flex flex-col flex-1 gap-4'>
      <div className='flex flex-col w-full flex-1'>
        <h1 className='text-center text-4xl font-bold'>ChatRoom</h1>
        <div className='flex-1'></div>
      </div>
      <form className='w-full flex gap-4'>
        <input className='shadow-full w-full px-4 py-2 rounded-md focus:outline-sky-600' />
        <button>
          <i className='fa-solid fa-paper-plane text-2xl hover:text-3xl'></i>
        </button>
      </form>
    </div>
  );
};
export default ChatRoom;

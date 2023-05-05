import { useState } from 'react';

const AddChapterForm = ({ onAddChapter }) => {
  const [chapters, setChapters] = useState([]);
  const [name, setName] = useState('');
  const [video, setVideo] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const newChapter = {
      id: chapters.length + 1,
      name,
      video,
    };
    setChapters([...chapters, newChapter]);
    onAddChapter(newChapter);
    setName('');
    setVideo('');
  };

  return (
    <div>
      <div className="mb-4">
        <label htmlFor="title" className="block text-gray-700 font-bold mb-2">
          Name
        </label>
        <input
          type="text"
          id="name"
          name="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"

        />
      </div>
      <div className="mb-4">
        <label htmlFor="video" className="block text-gray-700 font-bold mb-2">
          Video Url
        </label>
        <textarea
          id="video"
          name="video"
          value={video}
          onChange={(e) => setVideo(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"

        />
      </div>
      
      <button
        onClick={(e)=> handleSubmit(e)}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded"
      >
        Add Chapter
      </button> 

     
    </div>
  );
};

export default AddChapterForm;

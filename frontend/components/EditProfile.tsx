import { useState } from "react";
import { Dialog, Transition } from "@headlessui/react";

export default function EditProfileModal({ isOpen, closeModal }) {
  const [name, setName] = useState("");
  const [language, setLanguage] = useState("");
  const [about, setAbout] = useState("");

  const handleSaveChanges = () => {
    // Call an API or do something else to save changes to the user's profile
    closeModal();
  };

  return (
    <Transition show={isOpen} as={closeModal}>
      <Dialog
        onClose={closeModal}
        className="fixed z-10 inset-0 overflow-y-auto"
        aria-labelledby="modal-title"
        as="div"
      >
        <div className="min-h-screen px-4 text-center">
          <Transition.Child
            as={Dialog.Overlay}
            className="fixed inset-0 bg-black opacity-30"
          />
          <div className="inline-block w-full max-w-md p-6 my-8 overflow-hidden text-left align-middle transition-all transform bg-white shadow-xl rounded-2xl">
            <Dialog.Title
              as="h3"
              className="text-lg font-medium leading-6 text-gray-900"
              id="modal-title"
            >
              Edit Profile
            </Dialog.Title>
            <div className="mt-2">
              <label
                htmlFor="name"
                className="block text-sm font-medium text-gray-700"
              >
                Name
              </label>
              <input
                type="text"
                name="name"
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 focus:ring-opacity-50"
              />
            </div>
            <div className="mt-2">
              <label
                htmlFor="language"
                className="block text-sm font-medium text-gray-700"
              >
                Language
              </label>
              <input
                type="text"
                name="language"
                id="language"
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 focus:ring-opacity-50"
              />
            </div>
            <div className="mt-2">
              <label
                htmlFor="about"
                className="block text-sm font-medium text-gray-700"
              >
                About
              </label>
              <textarea
                name="about"
                id="about"
                value={about}
                onChange={(e) => setAbout(e.target.value)}
                className="block w-full mt-1 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-500 focus:ring-opacity-50"
              ></textarea>
            </div>
            <div className="mt-4 flex justify-end">
              <button
                type="button"
                className="inline-flex justify-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-indigo-500"
                onClick={handleSaveChanges}
              >
                Save Changes
              </button>
              <button
                type="button"
                className="inline-flex justify-center px-4 py-2 ml-4 text-sm font-medium text-gray-700 bg-gray-100 border border-gray-300 rounded-md hover:bg-gray-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-gray-500"
                onClick={closeModal}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      </Dialog>
    </Transition>
  );
}

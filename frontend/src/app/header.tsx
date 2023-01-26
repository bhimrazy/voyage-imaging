import React from "react";
import Link from "next/link";

type Props = {};

export default function Header({}: Props) {
  const content = {
    logo: {
      icon: (
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="h-6 w-6"
        >
          <path
            fillRule="evenodd"
            d="M2.25 4.125c0-1.036.84-1.875 1.875-1.875h5.25c1.036 0 1.875.84 1.875 1.875V17.25a4.5 4.5 0 11-9 0V4.125zm4.5 14.25a1.125 1.125 0 100-2.25 1.125 1.125 0 000 2.25z"
            clipRule="evenodd"
          />
          <path d="M10.719 21.75h9.156c1.036 0 1.875-.84 1.875-1.875v-5.25c0-1.036-.84-1.875-1.875-1.875h-.14l-8.742 8.743c-.09.089-.18.175-.274.257zM12.738 17.625l6.474-6.474a1.875 1.875 0 000-2.651L15.5 4.787a1.875 1.875 0 00-2.651 0l-.1.099V17.25c0 .126-.003.251-.01.375z" />
        </svg>
      ),
      title: (
        <>
          Voyage <span className="text-pink-600">Imaging</span>
        </>
      ),
    },

    menus: [
      {
        title: "Home",
        link: "/",
        active: true,
      },
      {
        title: "Our Service",
        link: "/",
      },
      {
        title: "About Us",
        link: "/",
      },
      {
        title: "Health News",
        link: "/",
      },
    ],
    button: "Login",
  };
  return (
    <header className="flex w-full py-6 border-b">
      <nav className="mx-auto flex w-full max-w-7xl flex-row items-center justify-between">
        {/* Logo */}
        <div className="flex cursor-pointer flex-row items-center space-x-2">
          <span className="text-yellow-600">{content?.logo?.icon}</span>
          <span className="text-2xl font-bold text-sky-800">
            {content?.logo?.title}
          </span>
        </div>
        {/* Menu Items */}
        <ul className="flex flex-row space-x-8">
          {content?.menus &&
            content?.menus.map((item, i) => (
              <Link href={item?.link} key={i}>
                <li
                  className={`${
                    item?.active ? "font-medium text-sky-700" : "text-sky-600"
                  } transition hover:text-sky-900`}
                >
                  {item?.title}
                </li>
              </Link>
            ))}
        </ul>

        {/* Buttons */}
        <button className="rounded-md bg-sky-900 px-6 py-3 font-semibold text-white transition hover:bg-sky-900/90 focus:outline-none">
          {content?.button}
        </button>
      </nav>
    </header>
  );
}

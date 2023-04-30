import "../styles/globals.css";
import Navbar from "../components/Navbar";
import { CookiesProvider } from "react-cookie";

export default function App({ Component, pageProps }) {
  return (
    <CookiesProvider>
      <Navbar/>
      <Component {...pageProps} />
    </CookiesProvider>
  );
}

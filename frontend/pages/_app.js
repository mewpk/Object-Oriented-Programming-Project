<<<<<<< HEAD
import '@/styles/globals.css'
import Layout from '@/component/Layout'
=======
import '../styles/globals.css'
>>>>>>> 30d30cdf4521aeb929ce72b5c9c9ccc04acf5056

export default function App({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}

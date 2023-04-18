import styles from "@/styles/Home.module.css"
import Image from "next/image"
import Link from "next/link"
import Head from "next/head"
export default function Home(){
  return(
    <>
    <Head>
      <title>Udemy</title>
    </Head>
    <div className={styles.main}>

      <h1 className={styles.title}>Udemy</h1>
      <Image src="/shopping.svg" width={500} height={500} alt="shopping" />
      <p className={styles.title}>welcome to Udemy</p>
      <Link href="/products" className={styles.btn}>view all course</Link>
    </div>
 
    </>
  )
}
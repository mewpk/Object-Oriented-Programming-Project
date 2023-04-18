import Link from "next/link"
import Image from "next/image"
// import Button from "next/button"
export default function Navbar(){
    return(
        <nav>
            <div className="logo">
                <Link href="/">Udemy</Link>
                <Link href="/categories">categories</Link>
            </div>
                <form action="/send-data-here" method="get">
                    <input
                        type="text"
                        id="roll"
                        name="roll"
                        required
                        minlength="10"
                        maxlength="20"
                        style={{height:"30px" ,width:"400px",borderRadius:"20px"}}
                    />
                    </form>           
           <Link href="/">Udemy Business</Link>
           <Link href="/about">Teach on Udemy</Link>
           <Link href="/products">
           <Image src="/cart.png" width={30} height={30} alt="logo"/>
           </Link>
           {/* <Button type="button" color="primary">Primary</Button> */}
        </nav>
    )
}
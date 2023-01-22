import './globals.css'
import { Poppins } from '@next/font/google';

const poppins = Poppins({ 
  weight:['100','200','300','400','500','600','700','800','900'],
  subsets: ['latin'] 
})
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={poppins.className}>
      {/*
        <head /> will contain the components returned by the nearest parent
        head.tsx. Find out more at https://beta.nextjs.org/docs/api-reference/file-conventions/head
      */}
      <head />
      <body>{children}</body>
    </html>
  )
}

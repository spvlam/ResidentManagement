import '@/app/ui/global.css';
import { inter } from '@/app/ui/fonts';
import Search from './ui/search';
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">

      <body className={`${inter.className} antialiased`}>
        {children}</body>
    </html>
  );
}

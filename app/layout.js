export const metadata = {
  title: 'BİTASA | Enterprise AI',
  description: 'Enterprise Intelligent System',
}

export default function RootLayout({ children }) {
  return (
    <html lang="tr">
      <body style={{ margin: 0, padding: 0, backgroundColor: '#212121' }}>
        {children}
      </body>
    </html>
  )
}

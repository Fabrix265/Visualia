export function descargarHTML(htmlContent, titulo = 'recurso') {
  const blob = new Blob([htmlContent], { type: 'text/html' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = `${titulo.replace(/\s+/g, '_')}.html`
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  URL.revokeObjectURL(url)
}

export function imprimirHTML(htmlContent) {
  const printWindow = window.open('', '_blank')
  if (!printWindow) {
    alert('Permití las ventanas emergentes para imprimir')
    return
  }

  printWindow.document.write(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Imprimir recurso</title>
      <style>
        @media print {
          body { margin: 0; padding: 0; }
          @page { margin: 1cm; }
        }
      </style>
    </head>
    <body>
      ${htmlContent}
    </body>
    </html>
  `)
  printWindow.document.close()
  
  printWindow.onload = () => {
    printWindow.print()
  }
}

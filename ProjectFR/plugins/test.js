import html2Canvas from 'html2canvas';
import JsPDF from 'jspdf';

export default {
    install(Vue, options) {
        Vue.prototype.getPdf = function (title, isShowPreviewFullTime) {
            html2Canvas(document.querySelector('#pdfDom'), {
                useCORS: true,
            }).then(function (canvas) {
                let pageWidth = 595.28
                let pageHeight = canvas.height / (canvas.width / 592.28)
                let pageData = canvas.toDataURL('image/jpeg', 1.0)
                let PDF = new JsPDF('p', 'pt', [canvas.height, canvas.width])
                PDF.addImage(pageData, 'JPEG', 0, 0, canvas.width, canvas.height)
                PDF.save(title + '.pdf')

            }
            )
        }
    }
}
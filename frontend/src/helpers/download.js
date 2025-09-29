import { safeBase64ToByteArray } from "@/helpers/formatters";


function downloadZipFileFromBase64(archiveName, archiveContent) {
    const decodedContent = safeBase64ToByteArray(archiveContent);
    const blob = new Blob([decodedContent], { type: 'application/zip' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = archiveName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


async function downloadBlobFileFromNameAndUrl(filename, fileurl) {
    const response = await fetch(fileurl)
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}


export {
    downloadZipFileFromBase64,
    downloadBlobFileFromNameAndUrl,
};

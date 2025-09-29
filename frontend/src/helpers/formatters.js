function convertToClientTimezone(timezone) {
    const utcDate = new Date(timezone).toLocaleString(); // UTC time
    return utcDate;
}

function formatTimezone(timezone) {
    let localDate = convertToClientTimezone(timezone);
    return localDate;
}

const padZeros = (num, length) => `${num}`.padStart(length, '0');

function base64ToByteArray(base64) {
    const binaryString = atob(base64);
    const byteArray = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
      byteArray[i] = binaryString.charCodeAt(i);
    }
    return byteArray;
}

function safeBase64ToByteArray(base64) {
    const sanitizedBase64 = base64.replace(/[^A-Za-z0-9+/=]/g, "");
    return base64ToByteArray(sanitizedBase64);
}

export {
    formatTimezone,
    padZeros,
    base64ToByteArray,
    safeBase64ToByteArray,
}

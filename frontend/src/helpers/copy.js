function jsonDeepCopy(obj) {
    return JSON.parse(JSON.stringify(obj));
}

export {
    jsonDeepCopy,
};

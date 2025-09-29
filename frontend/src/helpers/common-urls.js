const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const BACKEND_API_URL = `${BACKEND_URL}/api`;
const BACKEND_API_AUTH_URL = `${BACKEND_API_URL}/accounts`;

// User endpoints:
const userDataUrl = `${BACKEND_API_AUTH_URL}/get-user/`;
const passwordResetUrl = `${BACKEND_API_AUTH_URL}/password-reset/`;

// JWT endpoints:
const accessTokenUrl = `${BACKEND_API_AUTH_URL}/token/`;
const refreshTokenUrl = `${BACKEND_API_AUTH_URL}/token/refresh/`;
const verifyTokenUrl = `${BACKEND_API_AUTH_URL}/token/verify/`;

// Knox endpoints:
const loginUrl = `${BACKEND_API_AUTH_URL}/login/`;
const logoutUrl = `${BACKEND_API_AUTH_URL}/logout/`;
const logoutAllUrl = `${BACKEND_API_AUTH_URL}/logoutall/`;

// CRUDLB endpoints:
function modelCRUDLBUrlsMethods(modelBaseUrl, modelActions) {
    var modelUrls = {};
    for (let action of modelActions) {
        if (action.action === 'c') {
            modelUrls.create = {
                methods:   ['post'],
                url:       `${BACKEND_API_URL}/${modelBaseUrl}/create/`,
                multipart: action.multipart,
            };
        }
        if (action.action === 'r') {
            modelUrls.retrieve = {
                methods:   ['get'],
                url:       (id) => `${BACKEND_API_URL}/${modelBaseUrl}/retrieve/${id}/`,
                multipart: action.multipart,
            };
        }
        if (action.action === 'u') {
            modelUrls.update = {
                methods:   ['put','patch'],
                url:       (id) => `${BACKEND_API_URL}/${modelBaseUrl}/update/${id}/`,
                multipart: action.multipart,
            };
        }
        if (action.action === 'd') {
            modelUrls.delete = {
                methods:   ['delete'],
                url:       (id) => `${BACKEND_API_URL}/${modelBaseUrl}/destroy/${id}/`,
                multipart: action.multipart,
            };
        }
        if (action.action === 'l') {
            modelUrls.list = {
                methods:   ['get'],
                url:       `${BACKEND_API_URL}/${modelBaseUrl}/list/`,
                multipart: action.multipart,
            };
        }
        if (action.action === 'b') {
            modelUrls.bulk_create = {
                methods:   ['post'],
                url:       `${BACKEND_API_URL}/${modelBaseUrl}/bulk_create/`,
                multipart: action.multipart,
            };
        }
    }
    return modelUrls;
}

export {
    // Base urls:
    BACKEND_URL,
    BACKEND_API_URL,
    BACKEND_API_AUTH_URL,
    // User calls:
    userDataUrl,
    passwordResetUrl,
    // JWT Calls:
    accessTokenUrl,
    refreshTokenUrl,
    verifyTokenUrl,
    // Knox calls:
    loginUrl,
    logoutUrl,
    logoutAllUrl,
    // CRUD API Calls:
    modelCRUDLBUrlsMethods,
};

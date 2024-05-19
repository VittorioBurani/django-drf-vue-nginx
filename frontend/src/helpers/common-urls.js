const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

const BACKEND_API_URL = `${BACKEND_URL}/api`;
const BACKEND_API_AUTH_URL = `${BACKEND_API_URL}/auth`;

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

// CRUD endpoints:
const modelCRUDUrlsMethods = (modelName) => ({
    list:   {
        methods: ['get'],
        url:     `${BACKEND_API_URL}/${modelName}/list/`
    },
    detail: {
        methods: ['get'],
        url:     (id) => `${BACKEND_API_URL}/${modelName}/retrieve/${id}/`
    },
    create: {
        methods: ['post'],
        url:     `${BACKEND_API_URL}/${modelName}/create/`
    },
    update: {
        methods: ['put','patch'],
        url:     (id) => `${BACKEND_API_URL}/${modelName}/update/${id}/`
    },
    delete: {
        methods: ['delete'],
        url:     (id) => `${BACKEND_API_URL}/${modelName}/destroy/${id}/`
    },
});

export {
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
    modelCRUDUrlsMethods,
};

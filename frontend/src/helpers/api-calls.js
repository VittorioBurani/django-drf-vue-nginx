import axios from 'axios';
import {
    // User API Calls:
    userDataUrl,
    passwordResetUrl,
    // JWT API Calls:
    accessTokenUrl,
    refreshTokenUrl,
    verifyTokenUrl,
    // Knox API Calls:
    loginUrl,
    logoutUrl,
    logoutAllUrl,
} from './common-urls.js';


// Header utility:
const authHeaderHandler = (accessToken, method) => {
    let ret = {'Authorization': `Bearer ${accessToken}`};
    if (method !== 'get') ret['Content-Type'] = 'application/json';
    return ret
}

const knoxHeaderHandler = (accessToken, method) => {
    let ret = {'Authorization': `Token ${accessToken}`};
    if (method !== 'get') ret['Content-Type'] = 'application/json';
    return ret
}


// User API Calls:
const userDataApiCall = (accessToken) => axios.get(userDataUrl, {headers: authHeaderHandler(accessToken, 'get')});

const passwordResetApiCall = (accessToken, new_pwd, conf_pwd) => axios.post(
    passwordResetUrl,
    {
        new_password: new_pwd,
        confirm_password: conf_pwd,
    },
    {headers: authHeaderHandler(accessToken, 'post')},
);


// JWT API Calls:
const accessTokenApiCall = (username, password) => axios.post(
    accessTokenUrl,
    {
        username: username,
        password: password,
    },
    {headers: {'Content-Type': 'application/json'}},
);

const refreshTokenApiCall = (refreshToken) => axios.post(
    refreshTokenUrl,
    {
        refresh: refreshToken
    },
    {headers: {'Content-Type': 'application/json'}},
);

const verifyTokenApiCall = (accessToken) => axios.post(
    verifyTokenUrl,
    {
        token: accessToken
    },
    {headers: {'Content-Type': 'application/json'}},
);


// Knox API Calls:
const loginApiCall = (username, password) => axios.post(
    loginUrl,
    {
        username: username,
        password: password,
    },
    {headers: {'Content-Type': 'application/json'}},
);

const logoutApiCall = (accessToken) => axios.post(
    logoutUrl,
    {},
    {headers: knoxHeaderHandler(accessToken, 'post')},
);

const logoutAllApiCall = (accessToken) => axios.post(
    logoutAllUrl,
    {},
    {headers: knoxHeaderHandler(accessToken, 'post')},
);


// Export all the API calls:
export {
    // User API Calls:
    userDataApiCall,
    passwordResetApiCall,
    // JWT API Calls:
    accessTokenApiCall,
    refreshTokenApiCall,
    verifyTokenApiCall,
    // Knox API Calls:
    loginApiCall,
    logoutApiCall,
    logoutAllApiCall,
};

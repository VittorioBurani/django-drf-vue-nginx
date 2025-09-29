import axios from 'axios';
import { DB_MODEL_APIS } from './db-models.js';
import {
    // Base url for custom API Calls:
    BACKEND_API_URL,
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
    // CRUD API Calls:
    modelCRUDLBUrlsMethods,
} from './common-urls.js';


//////////////////////
// Header utilities //
//////////////////////

const authHeaderHandler = (accessToken, method, multipart=false) => {
    let ret = {'Authorization': `Bearer ${accessToken}`};
    if (method !== 'get') ret['Content-Type'] = multipart ? 'multipart/form-data' : 'application/json';
    return ret
}

const knoxHeaderHandler = (accessToken, method, multipart=false) => {
    let ret = {'Authorization': `Token ${accessToken}`};
    if (method !== 'get') ret['Content-Type'] = multipart ? 'multipart/form-data' : 'application/json';
    return ret
}


///////////////////
// JWT API Calls //
///////////////////

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


////////////////////
// Knox API Calls //
////////////////////

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


///////////////////////////////////
// Current Logged User API Calls //
///////////////////////////////////

const userDataApiCall = (accessToken) => axios.get(userDataUrl, {headers: knoxHeaderHandler(accessToken, 'get')});

const passwordResetApiCall = (accessToken, new_pwd, conf_pwd) => axios.post(
    passwordResetUrl,
    {
        new_password: new_pwd,
        confirm_password: conf_pwd,
    },
    {headers: knoxHeaderHandler(accessToken, 'post')},
);


////////////////////////////////
// DB Models CRUDLB API Calls //
////////////////////////////////

function composeCRUDLBApiCall(callName, httpMethod, url, multipart) {
    // RL actions
    if (httpMethod === 'get') {
        if (callName === 'list') {
            return (accessToken, params) => axios.get(url, {headers: knoxHeaderHandler(accessToken, httpMethod, multipart), params: params});
        } else {
            return (accessToken, id) => axios.get(url(id), {headers: knoxHeaderHandler(accessToken, httpMethod, multipart)});
        }
    }
    // CB actions
    if (httpMethod === 'post') {
        return (accessToken, data) => axios.post(url, data, {headers: knoxHeaderHandler(accessToken, httpMethod, multipart)});
    }
    // U actions
    if (httpMethod === 'put') {
        return (accessToken, id, data) => axios.put(url(id), data, {headers: knoxHeaderHandler(accessToken, httpMethod, multipart)});
    }
    if (httpMethod === 'patch') {
        return (accessToken, id, data) => axios.patch(url(id), data, {headers: knoxHeaderHandler(accessToken, httpMethod, multipart)});
    }
    // D action
    if (httpMethod === 'delete') {
        return (accessToken, id) => axios.delete(url(id), {headers: knoxHeaderHandler(accessToken, httpMethod, multipart)});
    }
}

const singleModelCRUDLBApiCalls = (modelBaseUrl, modelActions) => {
    let modelUrls = modelCRUDLBUrlsMethods(modelBaseUrl, modelActions);
    for (let [key, value] of Object.entries(modelUrls)) {
        if (value.methods.length === 1) {
            modelUrls[key] = composeCRUDLBApiCall(key, value.methods[0], value.url, value.multipart);
        } else {
            for (let method of value.methods) {
                modelUrls[`${method}_${key}`] = composeCRUDLBApiCall(key, method, value.url, value.multipart);
            }
        }
    }
    return modelUrls;
}

const modelAPIs = Object.fromEntries(DB_MODEL_APIS.map(model => [model.name.replaceAll('-', '_'), singleModelCRUDLBApiCalls(model.base_url, model.actions)]));


////////////////////////////////
// DB Models Custom API Calls //
////////////////////////////////

// ... To be added if any ...


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
    // CRUD API Calls:
    modelAPIs,
};

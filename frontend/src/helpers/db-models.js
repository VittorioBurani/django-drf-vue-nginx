/*
 * Each object exposes:
 * - name: The name of the model in URLs
 * - base_url: The base URL of the model
 * - actions: The standard CRUDLB actions available for the model
 *            (c = create, r = retrieve, u = update, d = delete, l = list, b = bulk_create)
 */

const DB_MODEL_NAMES = [
    // Example:
    // {
    //     name: 'model_name',
    //     base_url: '/model/url',
    //     actions: [
    //         {action: 'c', multipart: false},
    //         {action: 'r', multipart: false},
    //         {action: 'u', multipart: false},
    //         {action: 'd', multipart: false},
    //         {action: 'l', multipart: false},
    //         {action: 'b', multipart: false},
    //     ],
    // },
];

export {
    DB_MODEL_NAMES,
}

import * as yup from 'yup'
 export const schema=yup.object({
    nombre: yup.string().required("EL CAMPO ES OBLIGATORIO"),
    correo:yup.string().email("EL EMAIL NO ES VALIDO").required("ES OBLIGATIOR")
 })

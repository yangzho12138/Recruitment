import { USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGIN_FAIL } from '../contants/userConstants';
import axios from 'axios'

export const login = (username, password) => async(dispatch) => {
    try{
        dispatch({
            type: USER_LOGIN_REQUEST
        })

        // get token
        let config = {
            headers: {
                'Content-Type': 'application/json',
            }
        }

        const { data: token } = await axios.post('http://127.0.0.1:8000/api/users/token/',{ username, password }, config)

        console.log(token.access)
        // get userinfo
        config = {
            headers: {
                'Authorization': 'Bearer ' + token.access,
            }
        }

        const { data } = await axios.get('http://127.0.0.1:8000/api/users/getinfo', config)
        const userInfo = data.data
        userInfo.token = token
        
        console.log(data)
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: userInfo
        })

        localStorage.setItem('userInfo', JSON.stringify(data))
    }catch(error){
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: error.response && error.response.data.message ? error.response.data.message : error.message
        })
    }
}
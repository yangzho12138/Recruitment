import { USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGIN_FAIL, USER_LOGOUT, USER_REGISTER_REQUEST, USER_REGISTER_SUCCESS, USER_REGISTER_FAIL } from '../contants/userConstants';
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
        
        dispatch({
            type: USER_LOGIN_SUCCESS,
            payload: userInfo
        })

        localStorage.setItem('userInfo', JSON.stringify(userInfo))
    }catch(error){
        dispatch({
            type: USER_LOGIN_FAIL,
            payload: "Error: invalid username or password"
        })
    }
}

export const logout = () => (dispatch) => {
    localStorage.removeItem('userInfo')
    dispatch({ type: USER_LOGOUT})
}

export const register = (username, email, password, password_confirm) => async(dispatch) => {
    try{
        dispatch({
            type: USER_REGISTER_REQUEST
        })

        let config = {
            headers:{
                'Content-Type': "application/x-www-form-urlencoded"
            }
        }

        console.log(username, email, password, password_confirm)
        const response = await axios.post('http://127.0.0.1:8000/api/users/register', {
            username,
            email,
            password,
            password_confirm
        }, config)

        console.log(response)

        if(response.data.status !== 201){
            throw new Error(response.data.message)
        }

        dispatch({
            type: USER_REGISTER_SUCCESS
        })

        dispatch(login(username, password))

    }catch(error){
        console.log("error", error)
        dispatch({
            type: USER_REGISTER_FAIL,
            payload: error.toString()
        })
    }
}
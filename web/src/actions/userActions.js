import { USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGIN_FAIL, USER_LOGOUT, USER_REGISTER_REQUEST, USER_REGISTER_SUCCESS, USER_REGISTER_FAIL, USER_RESUME_UPDATE_REQUEST, USER_RESUME_UPDATE_SUCCESS, USER_RESUME_UPDATE_FAIL, USER_RESUME_REQUEST, USER_RESUME_SUCCESS, USER_RESUME_FAIL, USER_RESUME_RESET } from '../contants/userConstants';
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
    dispatch({ type: USER_LOGOUT })
    dispatch({ type: USER_RESUME_RESET })
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

        const response = await axios.post('http://127.0.0.1:8000/api/users/register', {
            username,
            email,
            password,
            password_confirm
        }, config)

        if(response.data.status !== 201){
            throw new Error(response.data.message)
        }

        dispatch({
            type: USER_REGISTER_SUCCESS
        })

        dispatch(login(username, password))

    }catch(error){
        dispatch({
            type: USER_REGISTER_FAIL,
            payload: error.toString()
        })
    }
}


export const getResume = () => async(dispatch, getState) => {
    try{
        console.log('get')
        dispatch({
            type: USER_RESUME_REQUEST
        })

        const { userLogin: {userInfo} } = getState()
        let config = {
            headers:{
                'Authorization': `Bearer ${userInfo.token.access}`
            }
        }

        const response = await axios.get('http://127.0.0.1:8000/api/users/resume', config)

        console.log(response)
        if(response.data.status !== 200){
            throw new Error(response.data.message)
        }

        dispatch({
            type: USER_RESUME_SUCCESS,
            payload: response.data.data
        })
    }catch(error){
        dispatch({
            type: USER_RESUME_FAIL,
            payload: error.toString()
        })
    }
}


export const updateResume = (resume, file) => async(dispatch, getState) => {
    try{
        dispatch({
            type: USER_RESUME_UPDATE_REQUEST
        })

        const { userLogin: {userInfo} } = getState()
        let config = {
            headers:{
                'Content-Type': "application/x-www-form-urlencoded",
                'Authorization': `Bearer ${userInfo.token.access}`
            }
        }

        let response = await axios.post('http://127.0.0.1:8000/api/users/resume', resume, config)

        console.log(response)
        if(response.data.status !== 201){
            throw new Error(response.data.message)
        }

        if(file){
            config = {
                headers:{
                    'Content-Type': 'multipart/form-data',
                    'Authorization': `Bearer ${userInfo.token.access}`
                }
            }
    
            response = await axios.post('http://127.0.0.1:8000/api/users/resume/upload', {
                file,
            }, config)
    
            console.log(response)
            if(response.data.status !== 200){
                throw new Error(response.data.message)
            }
        }


        dispatch({
            type: USER_RESUME_UPDATE_SUCCESS,
        })
    }catch(error){
        dispatch({
            type: USER_RESUME_UPDATE_FAIL,
            payload: error.toString()
        })
    }
}
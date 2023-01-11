import React, { useState, useEffect } from 'react'
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import { useSelector, useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { getResume, updateResume } from '../actions/userActions';

export const Resume = () => {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [phone, setPhone] = useState('')
    const [gender, setGender] = useState('')
    const [bornAddress, setBornAddress] = useState('')
    const [city, setCity] = useState('')
    const [degree, setDegree] = useState('')
    const [major, setMajor] = useState('')
    const [UU, setUU] = useState('')
    const [UGPA, setUGPA] = useState('')
    const [GU, setGU] = useState('')
    const [GGPA, setGGPA] = useState('')
    const [PU, setPU] = useState('')
    const [PGPA, setPGPA] = useState('')
    const [intro, setIntro] = useState('')
    const [workExp, setWorkExp] = useState('')
    const [projExp, setProjExp] = useState('')

    const dispatch = useDispatch()

    const data = {
        name,
        email,
        phone,
        gender,
        bornAddress,
        city,
        degree,
        major,
        UU,
        UGPA,
        GU,
        GGPA,
        PU,
        PGPA,
        intro,
        workExp,
        projExp
    }

    const userLogin = useSelector(state => state.userLogin)
    const { userInfo } = userLogin

    const userResumeInfo = useSelector(state => state.userResume)
    const { userResume } = userResumeInfo

    useEffect(() => {
        if(userResume){
            const resume = JSON.parse(userResume)
            const resumeInfo = resume[0].fields
            setName(resumeInfo.username)
            setEmail(resumeInfo.email)
            setPhone(resumeInfo.phone)
            setGender(resumeInfo.gender)
            setBornAddress(resumeInfo.born_address)
            setCity(resumeInfo.city)
            setDegree(resumeInfo.degree)
            setMajor(resumeInfo.major)
            setUU(resumeInfo.bachelor_school)
            setUGPA(resumeInfo.bachelor_GPA)
            setGU(resumeInfo.master_school)
            setGGPA(resumeInfo.master_GPA)
            setPU(resumeInfo.doctor_school)
            setPGPA(resumeInfo.doctor_GPA)
            setIntro(resumeInfo.candidate_introduction)
            setWorkExp(resumeInfo.work_experience)
            setProjExp(resumeInfo.project_experience)
        }else{
            dispatch(getResume())
        }
    }, [dispatch, userResume])

    const submitHandler = (e) => {
        e.preventDefault();
        dispatch(updateResume(data))
    }

    return(
        (userInfo ? (
            <>
                <Card className='mx-3 my-3'>
                    <Card.Body>
                        <h2>Online Resume</h2>
                        <Form onSubmit={submitHandler}>
                            <Card className='mx-3 my-3'>
                                <Card.Body>
                                    <h3>Basic Info</h3>
                                    <Form.Group as={Row} className="mb-3">
                                        <Form.Label column sm="1">
                                            Name*
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your name" value={name} onChange={e => setName(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="1">
                                            Email*
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control type='email' placeholder="Enter your email" value={email} onChange={e => setEmail(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="1">
                                            Phone*
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your phone" value={phone} onChange={e => setPhone(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <Form.Group  as={Row} className="mb-3">
                                        <Form.Label column sm="1">
                                            Gender
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your geneder" value={gender} onChange={e => setGender(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="1">
                                            Born in
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your born country" value={bornAddress} onChange={e => setBornAddress(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="1">
                                            City
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter city you live in" value={city} onChange={e => setCity(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <h3>Education Info</h3>
                                    <Form.Group as={Row} className="mb-3">
                                        <Form.Label column sm="3">
                                            Degree*
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter highest degree you earned" value={degree} onChange={e => setDegree(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="3">
                                            Major*
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your major" value={major} onChange={e => setMajor(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} className="mb-3">
                                        <Form.Label column sm="3">
                                            Undergraduate University or College
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your undergraduate university" value={UU} onChange={e => setUU(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="3">
                                            Undergraduate GPA
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your undergraduate GPA" value={UGPA} onChange={e => setUGPA(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} className="mb-3">
                                        <Form.Label column sm="3">
                                            Graduate University or College
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your graduate university" value={GU} onChange={e => setGU(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="3">
                                            Graduate GPA
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your graduate GPA" value={GGPA} onChange={e => setGGPA(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} className="mb-3">
                                        <Form.Label column sm="3">
                                            Phd University or College
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your Phd university" value={PU} onChange={e => setPU(e.target.value)}/>
                                        </Col>
                                        <Form.Label column sm="3">
                                            Phd GPA
                                        </Form.Label>
                                        <Col sm="3">
                                            <Form.Control placeholder="Enter your Phd GPA" value={PGPA} onChange={e => setPGPA(e.target.value)}/>
                                        </Col>
                                    </Form.Group>
                                    <h3>Experience</h3>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Self Introduction</Form.Label>
                                        <Form.Control placeholder="Please introduce yourself and explain why you are interested in our group" as="textarea" rows={3} value={intro} onChange={e => setIntro(e.target.value)}/>
                                    </Form.Group>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Work Experience</Form.Label>
                                        <Form.Control placeholder="Please including company name, time scope, your position and duty" as="textarea" rows={3} value={workExp} onChange={e => setWorkExp(e.target.value)}/>
                                    </Form.Group>
                                    <Form.Group className="mb-3">
                                        <Form.Label>Project Experience</Form.Label>
                                        <Form.Control as="textarea" placeholder="Please including project name, time scope, your position and duty" rows={3} value={projExp} onChange={e => setProjExp(e.target.value)}/>
                                    </Form.Group>
                                    * means you must fill out this field
                                    <br/>
                                    <Button variant="primary" type='submit' className='my-3'>
                                        Submit/Update Resume
                                    </Button>
                                </Card.Body>
                            </Card>
                        </Form>
                    </Card.Body>
                </Card>
                <br/>
                <Card className='mx-3 my-3'>
                    <Card.Body>
                        <h2>Upload Resume</h2>
                        <div> You can update your resume here directly (pdf version)</div>
                    </Card.Body>
                </Card>
            </>
        ) : (
            <Card className='mx-3 my-3'>
                <Card.Body>Please <Link to='/signin'>Login</Link> Before Uploading Your Resume</Card.Body>
            </Card>
        ))
    )
}
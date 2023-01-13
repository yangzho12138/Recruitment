import React, { useState } from "react";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

export const Data = () => {
    const [offerNum, setOfferNum] = useState(0)
    const [posNum, setPosNum] = useState(0)

    return(
        <>
            <Container>
                <div style={{fontSize: '200%', textAlign:'center', backgroundColor: '#333333'}}>We Want You!</div>
                <div className="leftTop">左1</div>
                <div className="middleTop">
                    <div className="num">{offerNum}</div>
                    <div className="num">{posNum}</div>
                    <div className="txt">Offers</div>
                    <div className="txt">Positions</div>
                </div>
                <div className="rightTop">右1</div>
                <br/>
                <div className="leftButtom">左2</div>
                <div className="middleButtom">中2</div>
                <div className="rightButtom">右2</div>
            </Container>
        </>
    )
}
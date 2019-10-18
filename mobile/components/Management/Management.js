import { Card, Container, Content, Text, Thumbnail } from 'native-base';
import { Col, Grid, Row } from 'react-native-easy-grid';
import Header from '../Header';
import PropTypes from 'prop-types';
import React from 'react';
import components from '../../native-base-theme/components';
import uri from '../../assets/profile.png';

const styles = {
  row: {
    justifyContent: 'center',
    padding: 3
  }
}

class Management extends React.Component {
    state = {
      userName:'',
      height: '',
      weight: '',
      gender: '',
      smoking: '',
      ethnicity: '',
      diseases: '',
      occupation: '',
      alcohol: '',
    };

    componentWillMount() {
      var that = this;
      fetch('http://127.0.0.1:5000/user/id/2').then(res => {
        return res.json();
      }).then(res => {that.setState(
        {
          ...res
        })
        console.log(this.state);
      }
      )
    }
    render() {
      return (
      <Container>
      <Content padder>
        <Header
          title='Me'
          align='center'
        />
        <Card >
          <Grid style={{ padding: 5}}>
            <Row>
              <Col size={10}></Col>
              <Col size={80} style={{ alignItems: 'center'}}>
                <Row style={{ alignItems: 'center'}}>
                    <Thumbnail
                      style={{ height:300, width: 300 }}
                      source={uri}
                    />
                </Row>
              </Col>
              <Col size={10}></Col>
            </Row>
            <Row>
              <Col size={100}>
                <Row style={styles.row} >
                  <Text alignSelf='center' style={{textAlign:'center', fontWeight:'bold'}}>
                    {this.state.userName}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center'>
                    Smoking: {this.state.smoking.toUpperCase()}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center'>
                    Alcohol: {this.state.alcohol.toUpperCase()}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center'>
                    Weight: {this.state.weight}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center'>
                  Height: {this.state.height}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center' style={{textAlign:'center'}}>
                    Ethnicity: {this.state.ethnicity}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center' style={{textAlign:'center'}}>
                    Gender: {this.state.gender.toUpperCase()}
                  </Text>
                </Row>
                <Row style={styles.row} >
                  <Text alignSelf='center' style={{textAlign:'center'}}>
                    Diseases: {this.state.disease == null ? 'None': this.state.disease}
                  </Text>
                </Row>
              </Col>
            </Row>
          </Grid>
        </Card>
      </Content>
    </Container>
    );
  }
};

Management.propTypes = {
    managementQuery: PropTypes.shape({
        loading: PropTypes.bool,
        error: PropTypes.shape(),
        management: PropTypes.arrayOf(PropTypes.shape()),
      }),
};

export default Management;

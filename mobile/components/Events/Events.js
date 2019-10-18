import { Actions } from 'react-native-router-flux';
import {
  Container, Content, Tab, Tabs,
} from 'native-base';
import Header from '../Header';
import PropTypes from 'prop-types';
import React from 'react';


const Events = () => {
  return (
    <Container>
      <Content padder>
        <Header hasTabs title="Posts" align='center'/>
        
      </Content>
    </Container>
  );
};

Events.propTypes = {
  eventsQuery: PropTypes.shape({
    loading: PropTypes.bool,
    error: PropTypes.shape(),
    events: PropTypes.arrayOf(PropTypes.shape()),
  }),
};

export default Events;

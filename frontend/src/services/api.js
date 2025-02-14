import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/spotify/";

export const fetchSpotifySongs = async (query) => {
    const response = await axios.get(`${API_URL}?query=${query}`);
    return response.data;
};

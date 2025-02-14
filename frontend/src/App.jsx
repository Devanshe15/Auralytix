import { useEffect, useState } from "react";
import { fetchSpotifySongs } from "./services/api";

function App() {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    fetchSpotifySongs("lofi").then(setSongs);
  }, []);

  return (
    <div>
      <h1>Auralytix - Spotify Music</h1>
      <ul>
        {songs.map((song, index) => (
          <li key={index}>
            <img src={song.album_image} alt={song.title} width="50" />
            <strong font-size= "1.5rem">{song.title}</strong> - {song.artist}
            <a href={song.spotify_url} target="_blank" rel="noreferrer">Listen</a>
            {song.preview_url && <audio controls src={song.preview_url}></audio>}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

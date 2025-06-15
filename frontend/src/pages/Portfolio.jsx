import { useState } from 'react';
import axios from 'axios';

const API = import.meta.env.VITE_API_BASE_URL;

export default function Portfolio() {
  const [designName, setDesignName] = useState('');
  const [file, setFile] = useState(null);
  const [items, setItems] = useState([]);
  const token = localStorage.getItem('token');

  const upload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("image", file);
    formData.append("design_name", designName);

    const res = await axios.post(`${API}/portfolio/upload`, formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'multipart/form-data'
      }
    });

    setItems(prev => [res.data, ...prev]);
    setDesignName('');
    setFile(null);
  };

  return (
    <div>
      <h2>🖼️ Portfolio</h2>
      <form onSubmit={upload} style={styles.form}>
        <input
          value={designName}
          onChange={(e) => setDesignName(e.target.value)}
          placeholder="Design name"
          required
        />
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          accept="image/*"
          required
        />
        <button type="submit">Upload</button>
      </form>

      <div style={styles.gallery}>
        {items.map((item) => (
          <div key={item.id} style={styles.card}>
            <img src={item.image_url} alt="" style={styles.img} />
            <h4>{item.design_name}</h4>
            <p><strong>Tags:</strong> {item.tags}</p>
            <p><strong>Caption:</strong> {item.caption}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  form: { marginBottom: '1rem', display: 'flex', gap: '1rem' },
  gallery: { display: 'flex', flexWrap: 'wrap', gap: '1rem' },
  card: { border: '1px solid #ccc', padding: '1rem', width: '250px' },
  img: { width: '100%', height: 'auto' },
};

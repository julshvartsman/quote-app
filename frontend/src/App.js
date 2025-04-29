import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState({ text: '', author: '' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

 
  const API_URL = 'https://quote-app-agt8.onrender.com/api/quote';
const fetchQuote = async () => {
    setLoading(true);
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      const data = await response.json();
      setQuote(data);
      setError(null);
    } catch (err) {
      setError('Could not fetch a quote. Please try again later.');
      console.error('Error fetching quote:', err);
    } finally {
      setLoading(false);
    }
  };

  // Fetch a quote when the component mounts
  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <div className="App">
      <h1>Quote of the Day</h1>
      
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p className="error">{error}</p>
      ) : (
        <div className="quote-container">
          <blockquote>
            <p>{quote.text}</p>
            {quote.author && <footer>— {quote.author}</footer>}
          </blockquote>
        </div>
      )}
      
      <button onClick={fetchQuote} disabled={loading}>
        {loading ? 'Loading...' : 'Get Quote'}
      </button>
    </div>
  );
}

export default App;

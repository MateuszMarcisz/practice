import Header from "./Header";
import Content from "./Content";
import {useState, useEffect} from "react";


function App() {
    const API_URL = 'https://jsonplaceholder.typicode.com/';

    const [list, setList] = useState([]);
    const [fetchError, setFetchError] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [resource, setResource] = useState('users');

    useEffect(() => {
        const fetchList = async () => {
            try {
                const response = await fetch(API_URL + resource);
                if (!response.ok) throw Error('Did not received expected data');
                const contentList = await response.json();
                setList(contentList);
                setFetchError(null);
            } catch (err) {
                setFetchError(err.message);
            } finally {
                setIsLoading(false);
            }
        }
        (async () => await fetchList())();
    }, [resource]);

    return (
        <div className="App">
            <Header className="Navbar"
                    setResource={setResource}
                    resource={resource}
            />
            <main>
                {isLoading && <p>Loading List...</p>}
                {fetchError && <p style={{color: 'red'}}>{`Error: ${fetchError}`}</p>}
                {!fetchError && !isLoading &&
                <Content
                    list={list}
                />}
            </main>
        </div>
    );
}

export default App;

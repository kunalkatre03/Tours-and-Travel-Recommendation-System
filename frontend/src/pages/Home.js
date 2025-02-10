import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

const Home = () => {
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  const handleSearch = () => {
    if (search.trim() !== "") {
      navigate(`/search?city=${search}`);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-5">
      <div className="max-w-4xl mx-auto text-center py-10">
        <h1 className="text-4xl font-bold text-blue-600">Discover Your Next Adventure</h1>
        <p className="text-lg text-gray-600 mt-2">Find the best destinations based on your interests.</p>
        <div className="flex justify-center mt-6">
          <Input
            type="text"
            placeholder="Search for a city..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-80 border border-gray-300 p-2 rounded-md"
          />
          <Button onClick={handleSearch} className="ml-2 bg-blue-500 text-white px-4 py-2 rounded-md">
            Search
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-4">
        {/** Dummy Destination Cards */}
        {["Goa", "Manali", "Jaipur"].map((place, index) => (
          <Card key={index} className="bg-white p-3 shadow-lg">
            <CardContent>
              <img src={`https://source.unsplash.com/300x200/?${place}`} alt={place} className="w-full rounded-md" />
              <h3 className="text-lg font-semibold mt-2">{place}</h3>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Home;

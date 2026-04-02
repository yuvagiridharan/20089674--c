class Element
{
    public int AtomicNumber;
    public string Name ;
    public string Symbol;
    public string Category;
    public string Description;

    public Element(int atomicNumber, string name, string symbol, string category, string description)
    {
        AtomicNumber = atomicNumber;
        Name = name;
        Symbol = symbol;
        Category = category;
        Description = description;
    }
    public void Display()
    {
        Console.WriteLine("Atomic Number:{0}", AtomicNumber);
        Console.WriteLine("Name:{0}", Name);
        Console.WriteLine("Category:{0}", Category);
        Console.WriteLine("Description:{0}", Description);
    }

    
}
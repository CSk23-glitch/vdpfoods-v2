import { useEffect, useState, useRef } from 'react';
import { Link } from 'react-router-dom';
import { Leaf, ChevronRight } from 'lucide-react';
import { motion } from 'framer-motion';
import Header from '../components/Header';
import { API_URL } from '../config';

interface DbCategory {
    id?: string;
    _id?: string;
    name: string;
    description: string;
    media_url?: string;
}

export default function CategoriesPage() {
    const [categories, setCategories] = useState<DbCategory[]>([]);
    const [loading, setLoading] = useState(true);
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                // First try to fetch actual explicit categories from the backend
                const res = await fetch(`${API_URL}/categories/`);
                if (res.ok) {
                    const data = await res.json();
                    if (data && data.length > 0) {
                        setCategories(data.filter((c: any) => c.is_active !== false));
                        setLoading(false);
                        return;
                    }
                }
                
                // Fallback: Infer categories from available products if explicit endpoint fails/is empty
                const prodRes = await fetch(`${API_URL}/products/`);
                if (prodRes.ok) {
                    const products = await prodRes.json();
                    const uniqueCats = Array.from(new Set(products.flatMap((p: { category_ids: string[] }) => p.category_ids || [])));
                    
                    const inferred: DbCategory[] = uniqueCats.map((catName: any) => {
                        const sampleProd = products.find((p: any) => p.category_ids?.includes(catName));
                        return {
                            name: catName,
                            description: `Explore our premium selection of fresh ${catName}.`,
                            media_url: sampleProd?.images?.[0] || 'https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80'
                        }
                    });
                    setCategories(inferred);
                }
            } catch (err) {
                console.error('Categories fetching error:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchCategories();
        window.scrollTo(0, 0);
    }, []);

    const resolveImageUrl = (url: string | undefined) => {
        if (!url) return '';
        if (url.startsWith('data:') || url.startsWith('http')) return url;
        return url;
    };

    if (loading) {
        return (
            <div className="h-screen w-full bg-[var(--color-bg)] flex items-center justify-center">
                <motion.div animate={{ rotate: 360 }} transition={{ duration: 2, repeat: Infinity, ease: "linear" }}>
                    <Leaf className="text-[var(--color-primary)]" size={64} />
                </motion.div>
            </div>
        );
    }

    return (
        <div ref={containerRef} className="relative bg-[var(--color-bg)] text-[var(--color-text)] font-sans min-h-screen selection:bg-[var(--color-primary)] selection:text-white overflow-hidden">
            <Header />

            <main className="relative z-10 pt-32 pb-20 px-6">
                <div className="max-w-7xl mx-auto">
                    <motion.div
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8 }}
                        className="text-center mb-16"
                    >
                        <h1 className="text-5xl md:text-7xl font-black text-[var(--color-text)] mb-6 font-serif">
                            Our <span className="italic text-[var(--color-primary)]">Collections</span>
                        </h1>
                        <p className="text-lg text-[var(--color-text)]/70 max-w-2xl mx-auto">
                            Select a category below to explore our specific harvests.
                        </p>
                    </motion.div>

                    {/* Classic Alternating Layout for Categories */}
                    <div className="flex flex-col gap-16 md:gap-32 w-full max-w-5xl mx-auto py-12">
                        {categories.map((category, index) => {
                            const isEven = index % 2 === 0;
                            const encodedCat = encodeURIComponent(category.name);
                            return (
                                <motion.div
                                    key={category.name}
                                    initial={{ opacity: 0, y: 50 }}
                                    whileInView={{ opacity: 1, y: 0 }}
                                    viewport={{ once: true, margin: "-100px" }}
                                    transition={{ duration: 0.8 }}
                                    className={`flex flex-col ${isEven ? 'md:flex-row' : 'md:flex-row-reverse'} items-center gap-12 md:gap-20`}
                                >
                                    <div className="w-full md:w-1/2 relative">
                                        {/* Decorative Background Blob */}
                                        <div className={`absolute -top-4 md:-top-6 ${isEven ? '-right-4 md:-right-8' : '-left-4 md:-left-8'} w-[calc(100%+1rem)] h-[calc(100%+2rem)] ${isEven ? 'bg-[var(--color-primary)]/10' : 'bg-[var(--color-secondary)]/10'} rounded-tl-[4rem] rounded-br-[4rem] rounded-tr-[1rem] rounded-bl-[1rem] -z-10`} />
                                        
                                        <Link to={`/products?category=${encodedCat}`} className="block relative z-10">
                                            <div className="aspect-[4/3] rounded-tl-[4rem] rounded-br-[4rem] rounded-tr-[1rem] rounded-bl-[1rem] overflow-hidden shadow-xl relative group bg-white/50">
                                                <img
                                                    src={resolveImageUrl(category.media_url)}
                                                    alt={category.name}
                                                    className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 mix-blend-multiply"
                                                />
                                            </div>
                                        </Link>
                                    </div>

                                    <div className="w-full md:w-1/2 flex flex-col items-start gap-4 px-4 md:px-0">
                                        <div className="w-8 h-8 rounded-full border border-[var(--color-secondary)] flex items-center justify-center text-[var(--color-secondary)] mb-2 transform -rotate-45">
                                            <Leaf size={14} />
                                        </div>
                                        
                                        <Link to={`/products?category=${encodedCat}`}>
                                            <h2 className="text-5xl md:text-6xl font-serif text-[var(--color-text)] font-black leading-none hover:text-[var(--color-primary)] transition-colors tracking-tight">
                                                {category.name}
                                            </h2>
                                        </Link>
                                        
                                        <p className="text-[var(--color-text)]/70 text-lg md:text-xl leading-relaxed mt-4 line-clamp-3">
                                            {category.description || `Browse all our high-quality ${category.name} guaranteed fresh from our farms.`}
                                        </p>
                                        
                                        <div className="mt-8">
                                            <Link 
                                                to={`/products?category=${encodedCat}`}
                                                className="group inline-flex items-center gap-3 bg-[var(--color-primary)] text-white px-8 py-4 rounded-full font-bold uppercase tracking-widest text-xs hover:bg-[var(--color-text)] transition-colors shadow-lg"
                                            >
                                                Explore Collection
                                                <ChevronRight size={16} className="group-hover:translate-x-1 transition-transform" />
                                            </Link>
                                        </div>
                                    </div>
                                </motion.div>
                            );
                        })}
                    </div>
                </div>
            </main>

            <footer className="relative z-10 w-full border-t border-[var(--color-border)] bg-[var(--color-bg)] py-16 text-center">
                <div className="flex flex-col items-center gap-4">
                    <Leaf className="text-[var(--color-primary)]" size={40} />
                    <h2 className="text-2xl font-serif text-[var(--color-text)] italic">Videeptha Foods</h2>
                    <p className="text-[var(--color-text)]/60 font-light">© 2026 Videeptha Foods. Rooted in Nature.</p>
                </div>
            </footer>
        </div>
    );
}

import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8">
      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-6xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent"
      >
        SkillX
      </motion.h1>
      
      <p className="text-xl text-slate-400 mb-8 text-center">
        اتعلم أي مهارة بالذكاء الاصطناعي
      </p>
      
      <Link to="/dashboard">
        <button className="bg-purple-600 hover:bg-purple-700 px-8 py-3 rounded-lg text-lg font-semibold transition">
          ابدأ الآن
        </button>
      </Link>
    </div>
  )
}

export default Home
